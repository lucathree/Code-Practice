const modal = $(".black-bg")
modal.hide()

$("#push-button").on('click', function(){
  modal.show()
})

$("#close").on('click', function(){
  modal.hide()
})