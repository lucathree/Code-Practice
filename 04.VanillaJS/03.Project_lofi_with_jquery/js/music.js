var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

let player;
function onYouTubeIframeAPIReady() {
    player = new YT.Player('ytplayer', {
        height: '0',
        width: '0',
        videoId: '5qap5aO4i9A',
        playerVars: {
            autoplay: 1,
        }
    });
}

const CHANNEL_IDS = [
    {'channelName': 'lofi hip hop radio - beats to relax/study to',
    'videoId': "5qap5aO4i9A"},
    {'channelName': 'jazz/lofi hip hop radio chill beats to relax/study to [LIVE 24/7]',
    'videoId': "kgx4WGK0oNU"},
    {'channelName': 'lofi hip hop radio - beats to sleep/chill to',
    'videoId': "DWcJFNfaw9c"},
    {'channelName': 'coffee shop radio // 24/7 lofi hip-hop beats',
    'videoId': "-5KAN9_CzSA"},
    {'channelName': 'Smoke Chill - Lofi hip hop ~ Stress relief, Relaxing music',
    'videoId': "_JOUoxdjPMU"}
]

const playButton = document.querySelector("#play");
const pauseButton = document.querySelector("#pause");
const nextButton = document.querySelector("#next");

playButton.addEventListener("click", function(){
    player.playVideo();
});

pauseButton.addEventListener("click", function(){
    player.pauseVideo();
});

let currentChannel = 0;
nextButton.addEventListener("click", function(){
    if (currentChannel >= CHANNEL_IDS.length) {
        currentChannel = 0;
    } else {
        currentChannel += 1
    }
    player.loadVideoById(CHANNEL_IDS[currentChannel].videoId);
    const channelName = document.querySelector("#channelName");
    channelName.innerText = CHANNEL_IDS[currentChannel].channelName;
});


