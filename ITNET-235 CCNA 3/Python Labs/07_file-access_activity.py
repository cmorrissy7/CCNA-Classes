# Open the devices.txt file
file = open("devices.txt", "a")

# Create while loop that asks user for a new device, exits the program if user
# types "exit", and appends the file with the new device name
while True:
    newItem = input("Enter device name: ")
    if newItem == "exit":
        print("All done!")
        break
    else:
        file.write(newItem + "\n")

# Close the file
file.close()
