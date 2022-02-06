def tower(n,s,d,h):
    if n == 1:
        print(f"move plate {n} from {s} to {d}")
        return
    else:
        tower(n-1,s,h,d)
        print(f"move plate {n} from {s} to {d}")
        tower(n-1,h,d,s)
        return

tower(2,"SOURCE","DESTINATION","HELPER")



