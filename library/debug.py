from monitor.models import Log


def debug(source, level, msg):
    if level == 0:
        Log.objects.create(
            source=source,
            level="Info",
            message="INFO: " + msg
        )
        print("INFO: " + msg)
    elif level == 1:
        Log.objects.create(
            source=source,
            level="Warning",
            message="WARNING: " + msg
        )
        print("WARNING: " + msg)
    else:
        Log.objects.create(
            source=source,
            level="Error",
            message="ERROR: " + msg
        )
        print("ERROR: " + msg)
