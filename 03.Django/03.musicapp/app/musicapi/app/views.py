import random
from typing import Union
from requests.exceptions import ConnectionError, HTTPError

from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from .serializers import SampleRequestSerializer
from .models import Samples


@csrf_exempt
@swagger_auto_schema(
    method='post',
    operation_summary="샘플 조합 반환",
    operation_description="입력된 메타데이터에 맞는 샘플 목록을 조합하여 반환합니다.",
    request_body=SampleRequestSerializer,
    responses={
        '200': openapi.Response(description='요청 성공'),
        '204': openapi.Response(description='적합한 샘플을 찾을 수 없음'),
        '400': openapi.Response(description='잘못된 형식의 요청'),
        '500': openapi.Response(description='내부 서버 오류'),
    },
)
@api_view(['POST'])
def match_sample(request: HttpRequest) -> Response:
    serializer: SampleRequestSerializer = SampleRequestSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
    except (ConnectionError, HTTPError) as error:
        return Response({'detail': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except ValidationError as error:
        return Response({'detail': str(error)}, status=status.HTTP_400_BAD_REQUEST)

    metadata: dict[str, object] = serializer.validated_data
    tracks: list[dict[str, object]] = metadata["tracks"]
    for index, track in enumerate(tracks):
        if track['is_primary'] == True:
            primary_track: dict[str, Union[str, list[str], bool]] = tracks.pop(index)
            break

    primary_request_params: dict[str, Union[list[str], int]] = {
        'genre': metadata['genre'],
        'role': primary_track['role'],
        'key': metadata['keys'],
        'time_signature': metadata['time_signatures'],
        'min_bpm': metadata['bpm'][0],
        'max_bpm': metadata['bpm'][1] if len(metadata['bpm']) == 2 else metadata['bpm'][0],
        'page': 1,
        'per_page': 100
    }
    try:
        primary_samples: Samples = Samples(primary_request_params, primary_track['instruments'])
    except (ConnectionError, HTTPError) as error:
        return Response({'detail': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    if primary_samples.total == 0:
        return Response({'detail': 'There is no matching sample for primary track'}, status=status.HTTP_204_NO_CONTENT)

    primary_sample: dict[str, Union[str, int]] = random.choice(primary_samples.items)

    items: list[dict[str, Union[str, int]]] = [primary_sample]
    for track in tracks:
        secondary_request_params: dict[str, Union[list[str], int]] = {
            'genre': metadata['genre'],
            'role': track['role'],
            'key': primary_sample['key'],
            'time_signature': primary_sample['time_signature'],
            'min_bpm': primary_sample['bpm'],
            'max_bpm': primary_sample['bpm'],
            'page': 1,
            'per_page': 100
        }
        if track['role'] == 'drums':
            del secondary_request_params['key']
        
        try:
            secondary_samples: Samples = Samples(secondary_request_params, track['instruments'])
        except (ConnectionError, HTTPError) as error:
            return Response({'detail': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        if secondary_samples.total > 0:
            sample: dict[str, Union[str, int]] = random.choice(secondary_samples.items)
            items.append(sample)
        else:
            continue

    return Response({'total': len(items), 'items': items}, status=status.HTTP_200_OK)

    
