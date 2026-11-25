is_online = True
has_new_files = True
force_sync = False
is_paused = False

if is_online and not has_new_files and (force_sync or is_paused):
    print("Synchronisieren")
else:
    print("Warten")
