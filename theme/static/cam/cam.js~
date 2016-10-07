/*window.onload = function() {

  // Normalize the various vendor prefixed versions of getUserMedia.
  navigator.getUserMedia = (navigator.getUserMedia ||
                            navigator.webkitGetUserMedia ||
                            navigator.mozGetUserMedia || 
                            navigator.msGetUserMedia);
// Check that the browser supports getUserMedia.
// If it doesn't show an alert, otherwise continue.
if (navigator.getUserMedia) {
  // Request the camera.
  navigator.getUserMedia(
    // Constraints
    {
      video: true
    },

    // Success Callback
    function(localMediaStream) {
			// Get a reference to the video element on the page.
			var vid = document.getElementById('camera-stream');

			// Create an object URL for the video stream and use this 
			// to set the video source.
			vid.src = window.URL.createObjectURL(localMediaStream);

    },

    // Error Callback
    function(err) {
      // Log the error to the console.
      console.log('The following error occurred when trying to use getUserMedia: ' + err);
    }
  );

} else {
  alert('Sorry, your browser does not support getUserMedia');
}
}*/




// Put event listeners into place
		window.addEventListener("DOMContentLoaded", function() {
			// Grab elements, create settings, etc.
			var canvas = document.getElementById("canvas"),
				context = canvas.getContext("2d"),
				video = document.getElementById("camera-stream"),
				videoObj = { "video": true },
				errBack = function(error) {
					console.log("Video capture error: ", error.code); 
				};

			// Put video listeners into place
			if(navigator.getUserMedia) { // Standard
				navigator.getUserMedia(videoObj, function(stream) {
					video.src = stream;
					video.play();
				}, errBack);
			} else if(navigator.webkitGetUserMedia) { // WebKit-prefixed
				navigator.webkitGetUserMedia(videoObj, function(stream){
					video.src = window.webkitURL.createObjectURL(stream);
					video.play();
				}, errBack);
			} else if(navigator.mozGetUserMedia) { // WebKit-prefixed
				navigator.mozGetUserMedia(videoObj, function(stream){
					video.src = window.URL.createObjectURL(stream);
					video.play();
				}, errBack);
			}

			// Trigger photo take
			document.getElementById("snap").addEventListener("click", function() {
				context.drawImage(video, 0, 0, 440, 280);
				var image = document.getElementById("imagetocrop");
				image.src = canvas.toDataURL();
				//alert( canvas.toDataURL()+"");
				//document.getElementById('image-to-crop').drawImage(image	);

			});
		}, false);
