import re

pattern = r'^https://[\w \s .]*$'  # Regular expression pattern for a valid URL

# with open('.\\OJT_ASSIGNMENT\\Programs\\Fourth_paper\\input.txt', "r") as input_file:          # Read URLs from input file
with open('input.txt', "r") as input_file:          # Read URLs from input file
    urls = input_file.read().splitlines()


# with open('.\\OJT_ASSIGNMENT\\Programs\\Fourth_paper\\output.txt', "w") as output_file:        # Verify each URL and write output to file
with open('output.txt', "w") as output_file:        # Verify each URL and write output to file

    for i, url in enumerate(urls):
        # print(i)
        # print(url)
        if re.match(pattern, url):
            output_file.write(f"{i+1}. {url} valid \n")
            print(f"{url}, valid \n")
        else:
            output_file.write(f"{i+1}.{url} invalid \n")
            print(f"{url}, invalid \n")

