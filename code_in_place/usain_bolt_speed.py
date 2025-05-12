SPEED = 10.44

def main():
    while True:
        time_str = input("Run time (s) ")
        time = float(time_str)
        Distance = SPEED * time
        print(f"Usain Bolt runs {Distance} meters in {time_str} seconds")
if __name__ == "__main__":
    main()