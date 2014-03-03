GoogleBeam
==========

Order your Raspberry Pi to capture images and upload them to your Google Drive account via Tweeting specific Hashtags. Built for the Arabnet Code and Design Day

### Hastags

+ #GBeamCam : Will order the pi to capture and image and upload it to Twitter
+ #GBeamSave : Will order the pi to capture an image and upload it to Google Drive

### Configuration:

Edit the config.js file with your credentials and tokens. Keep it confidential

```
	ntwitter:{
		consumer_key: 'YOUR_CONSUMER_KEY',
		consumer_secret: 'YOUR_CONSUMER_SECRET',
		access_token_key: 'ACCESS_TOKEN',
		access_token_secret: 'ACCESS_TOKEN_SECRET'
	},
	tumw:{
		consumer_key: 'YOUR_CONSUMER_KEY',
		consumer_secret: 'YOUR_CONSUMER_SECRET',
		token: 'ACCESS_TOKEN',
		token_secret: 'ACCESS_TOKEN_SECRET'
	},
	drive:{
		username: 'YOU_USERNAME',
		password: 'YOUR_PASSWORD'
	}
```

###Installation

```
  npm install googlebeam
```

###Contributors
+ [Raghd Hamzeh](https://github.com/rhamzeh)
+ [Donald Derek](https://github.com/DonaldDerek)

### License

(The MIT License)

Copyright (c) 2014 Donald Derek Haddad, Kifah Daher. 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


