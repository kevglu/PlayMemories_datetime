#  I cannot install the Python-Image-Converter because it runs on old python and I am too lazy to install another python version
# I just run it from here 
import importlib
pic = importlib.import_module("Python-Image-Converter.raw_image_converter.utils")

# works
pic.convert_raw(file = 'D:\\Users\\Kevin\\Pictures\\temp\\DSC08075.ARW', srcDir='D:\\Users\\Kevin\\Pictures\\temp', tgtDir='D:\\Users\\Kevin\\Pictures\\temp', extension=".jpg", resolution=("100%", "100%"))


# # find files to convert
#     try:
#         with concurrent.futures.ProcessPoolExecutor() as executor:
#             print(
#                 "Started conversion at : "
#                 + datetime.now().time().strftime("%H:%M:%S")
#                 + "\n"
#             )
#             print("Converting -> " + srcDir + " Directory !\n")
#             for file in os.listdir(srcDir):
#                 file = file.lower()
#                 if image_not_exists(file, tgtDir, args.ext):
#                     type = check_file_type(file)
#                     if "RAW" == type:
#                         executor.submit(
#                             convert_raw,
#                             file,
#                             srcDir,
#                             tgtDir,
#                             args.ext,
#                             resolution,
#                         )

#                     if "NOT_RAW" == type:
#                         executor.submit(
#                             convert_file,
#                             file,
#                             srcDir,
#                             tgtDir,
#                             args.ext,
#                             resolution,
#                         )
#                 else:
#                     print(
#                         f"{Fore.GREEN}File "
#                         + file
#                         + f" is already converted!{Style.RESET_ALL}"
#                         + " \n "
#                     )

#         print(
#             f"{Fore.GREEN}Converted Images are stored at - > "
#             + os.path.abspath(tgtDir)
#             + f"{Style.RESET_ALL}"
#         )

#         if args.delete_source_directory:
#             delete_directory(srcDir)

#     except Exception as e:
#         print(f"{Fore.RED}ERROR IN APPLICATION{Style.RESET_ALL}" + e)