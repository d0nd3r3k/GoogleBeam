/**
 * Module dependecies
 */

var path = require('path');
var config = require('./config.js')['ntwitter'];
var twitter = require('ntwitter');
var controller = require('./controller.js');

//Twitter API Config
var twit = new twitter(config); 

// Twitter symbols array
var watch = ['#GBeamCam','#GBeamSave'];
 
twit.verifyCredentials(function (err, data) {
    if(err) console.log(err);
})
.stream('user', {track:watch}, function(stream) {
	console.log("Twitter stream is ready and waiting for inc tweets...")
	stream.on('data', function (data) {
		
		if (data.text !== undefined) {

			var name = data.user.screen_name;
			var hashtags = data.entities.hashtags;

			var options = {cam: false,save: false}

			for(var i=0,l=hashtags.length;i<l;i++){
				if(hashtags[i].text.toLowerCase() == 'gbeamcam') options.cam = true;
				if(hashtags[i].text.toLowerCase() == 'gbeamsave') options.save = true;
			}
			if(options.cam){
				if(options.save) controller.shoot(name, true);
				else controller.shoot(name, false);
			}
		}
	});

	stream.on('error', function (err, code) {
		console.log("err: "+err+" "+code)
	});
});

