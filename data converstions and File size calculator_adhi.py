# Sound File Calculator

def Sound_file_size():

    print("\n===== SOUND FILE CALCULATOR =====")

    Sample_rate = int(input("Enter the sample rate (in Hz): "))

    Bit_depth = int(input("Enter the bit depth (in bits): "))

    Channels = int(input("Enter the number of channels (1 for mono, 2 for stereo): "))

    duration = int(input("Enter the duration of the audio file (in seconds): "))

    Data_type = input(
        "Enter the data type (bits or bit, bytes or byte, kilobytes or kb, megabytes or mb, gigabytes or gb): "
    ).lower()

    Sound_file_size = Sample_rate * Bit_depth * Channels * duration

    if Data_type == "bits" or Data_type == "bit":
        print(f"The size of the sound file is {Sound_file_size} bits.")

    elif Data_type == "bytes" or Data_type == "byte":
        print(f"The size of the sound file is {Sound_file_size / 8} bytes.")

    elif Data_type == "kilobytes" or Data_type == "kb":
        print(f"The size of the sound file is {Sound_file_size / (8 * 1024)} kilobytes.")

    elif Data_type == "megabytes" or Data_type == "mb":
        print(f"The size of the sound file is {Sound_file_size / (8 * 1024 * 1024)} megabytes.")

    elif Data_type == "gigabytes" or Data_type == "gb":
        print(f"The size of the sound file is {Sound_file_size / (8 * 1024 * 1024 * 1024)} gigabytes.")

    else:
        print("Invalid data type.")


# Image File Calculator

def Image_file_calculator():

    print("\n===== IMAGE FILE CALCULATOR =====")

    Width = int(input("Enter the width (in pixels): "))

    Height = int(input("Enter the height (in pixels): "))

    colour_depth = int(input("Enter the colour depth (in bits): "))

    Data_type = input(
        "Enter the data type (bits or bit, bytes or byte, kilobytes or kb, megabytes or mb, gigabytes or gb): "
    ).lower()

    Image_file_size = Width * Height * colour_depth

    if Data_type == "bits" or Data_type == "bit":
        print(f"The size of the image file is {Image_file_size} bits.")

    elif Data_type == "bytes" or Data_type == "byte":
        print(f"The size of the image file is {Image_file_size / 8} bytes.")

    elif Data_type == "kilobytes" or Data_type == "kb":
        print(f"The size of the image file is {Image_file_size / (8 * 1024)} kilobytes.")

    elif Data_type == "megabytes" or Data_type == "mb":
        print(f"The size of the image file is {Image_file_size / (8 * 1024 * 1024)} megabytes.")

    elif Data_type == "gigabytes" or Data_type == "gb":
        print(f"The size of the image file is {Image_file_size / (8 * 1024 * 1024 * 1024)} gigabytes.")

    else:
        print("Invalid data type.")


def File_size_conversion():

    value = float(input("Enter the value to convert: "))
    unit_from = input("Enter the unit to convert from (bits, bytes, kilobytes, megabytes, gigabytes): ").lower()
    unit_to = input("Enter the unit to convert to (bits, bytes, kilobytes, megabytes, gigabytes): ").lower()

    # Convert the value to bits first
    if unit_from == "bits" or unit_from == "bit":
        bits = value
    elif unit_from == "bytes" or unit_from == "byte":
        bits = value * 8
    elif unit_from == "kilobytes" or unit_from == "kb":
        bits = value * 8 * 1024
    elif unit_from == "megabytes" or unit_from == "mb":
        bits = value * 8 * 1024 * 1024
    elif unit_from == "gigabytes" or unit_from == "gb":
        bits = value * 8 * 1024 * 1024 * 1024
    else:
        print("Invalid input unit.")
        return

    # Convert the data to the desired unit
    if unit_to == "bits" or unit_to == "bit":
        converted_value = bits
    elif unit_to == "bytes" or unit_to == "byte":
        converted_value = bits / 8
    elif unit_to == "kilobytes" or unit_to == "kb":
        converted_value = bits / (8 * 1024)
    elif unit_to == "megabytes" or unit_to == "mb":
        converted_value = bits / (8 * 1024 * 1024)
    elif unit_to == "gigabytes" or unit_to == "gb":
        converted_value = bits / (8 * 1024 * 1024 * 1024)
    else:
        print("Invalid output unit.")
        return

    print(f"{value} {unit_from} = {converted_value} {unit_to}")


# Main Menu
while True:

    print("\n===== DATA SIZE CALCULATOR =====")
    print("1. Sound File Calculator")
    print("2. Image File Calculator")
    print("3. File_size_conversion")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        Sound_file_size()

    elif choice == "2":
        Image_file_calculator()

    elif choice == "3":
        File_size_conversion()

    elif choice == "4":
        print("Program closed.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

    retry = input("Do you want to try again? (y/n): ")

    if retry.lower() != "y":
        print("Program closed.")
        break
