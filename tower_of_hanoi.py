def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from rod {source} to rod {destination}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from rod {source} to rod {destination}")
    tower_of_hanoi(n - 1, auxiliary, destination, source)


num_disks = 3
tower_of_hanoi(num_disks, 'S', 'D', 'A')


