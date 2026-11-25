is_online = False
has_new_files = False
force_sync = True
is_paused = False

if is_online and has_new_files or force_sync and not is_paused:
    print("Synchronisieren")
else:
    print("Warten")
