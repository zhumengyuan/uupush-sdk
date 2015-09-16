# uupush-sdk

## sample

    from uupush.push import UUPush
    app_id = ""
    app_secret = ""
    channel = ""
    context = {}
	ttl = 0
    UUPush(app_id, app_secret).send(channel, context, ttl)
	apns = {
		"alert": "new",
		"badge": 1,
        "sound": "beep.wav",
        "content_available": False,
	}
    UUPush(app_id, app_secret).send(channel, context, ttl, apns)
