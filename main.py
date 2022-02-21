
import os
from random_password_generator import PasswordGenerator as Pg


DASHES = "-------------------------------------------------------------------"
PREPEND = "\t"
INDICATOR = "---> "
PASSWORD_STORAGE = "hashed_passwords_storage.txt"
DELIMITER = ", "
TAG_MIN_LENGTH = 2
TAG_MAX_LENGTH = 15


def write_to_file(tag, hash_value):
    """Writes the given parameters to password storage text file.

    Parameters:
        tag: a name to distinguish the hashed password.
        hash_value: a hashed version of a plain password.

    Returns:
        None
    """

    file_obj = open(PASSWORD_STORAGE, "a+")
    file_obj.write(tag + DELIMITER + hash_value + "\n")
    file_obj.close()


def get_user_input(template):
    """Asks users for an input while displaying the given parameter template.

    Parameters:
        template: a predefined formatted message to display.

    Returns:
        string: entered input as string after stripping.
    """

    return input(template).strip()


def get_tag():
    """Asks users to enter an alphanumeric tag for their password. Tag must be
    2-15 characters long and alphanumeric otherwise keep asks for tag.

    Returns:
        string: tag name entered by user.
    """

    while True:
        template = PREPEND + "Please enter an alphanumeric tag (2-15): "
        user_input = get_user_input(template)

        if len(user_input) < TAG_MIN_LENGTH or len(user_input) > TAG_MAX_LENGTH:
            print(PREPEND + INDICATOR + "Length of a tag must be in "
                                        "2-15 characters.")
        elif not user_input.isalnum():
            print(PREPEND + INDICATOR + "Tag must be an alphanumeric value.")
        else:
            return user_input


def get_others_count(template, _min, _max, error_msg, missmatch_msg):
    """A multipurpose function to receive integer input from the users by
    displaying the predefined template. User input must be in the range
    provided the _min and _max parameters otherwise appropriate error message
    is displayed.

    Parameters:
        template: a predefined formatted message to display.
        _min: user input must be same or greater.
        _max: user input must be same or smaller.
        error_msg: a message to  display if the input is not digit.
        missmatch_msg: a message to display if the input not in _min and _max.

    Returns:
        integer: user input as an integer.
    """

    while True:
        user_input = get_user_input(template)
        if not user_input.isdigit():
            print(error_msg)
        elif int(user_input) < _min or int(user_input) > _max:
            print(missmatch_msg)
        else:
            return int(user_input)


def generate_password():
    """A function which handle generating a random password using the
    PasswordGenerator class and creates multiple templates to asks for user
    input. Once all user inputs are gathered it and a password is generated
    it writes the hashed password to password storage file along with the tag.

    Returns:
        None
    """

    tag = None
    uppercase_count = None
    lowercase_count = None
    digits_count = None
    punctuation_count = None

    print(DASHES)
    print(PREPEND + "In process of generating a random password ...")
    print(DASHES)

    tag = get_tag()

    letters_template = PREPEND + "Please enter # of {} letters ({}-{}): "
    non_digit_temp = PREPEND + INDICATOR + "Please enter a single digit only."
    criteria_template = PREPEND + INDICATOR + "Number does match the criteria."

    upper_template = letters_template.format("uppercase", Pg.MIN_UPPER,
                                             Pg.MIN_UPPER + Pg.MIN_UPPER)
    uppercase_count = get_others_count(upper_template, Pg.MIN_UPPER,
                                       Pg.MIN_UPPER + Pg.MIN_UPPER,
                                       non_digit_temp, criteria_template)

    lower_template = letters_template.format("lowercase", Pg.MIN_LOWER,
                                             Pg.MIN_LOWER + Pg.MIN_LOWER)
    lowercase_count = get_others_count(lower_template, Pg.MIN_UPPER,
                                       Pg.MIN_UPPER + Pg.MIN_UPPER,
                                       non_digit_temp, criteria_template)

    other_template = PREPEND + "Please enter # of {} ({}-{}): "

    digits_template = other_template.format("digits", Pg.MIN_DIGITS,
                                            Pg.MIN_DIGITS + Pg.MIN_DIGITS)
    digits_count = get_others_count(digits_template, Pg.MIN_DIGITS,
                                    Pg.MIN_DIGITS + Pg.MIN_DIGITS,
                                    non_digit_temp, criteria_template)

    punctuation_template = other_template.format("punctuations", Pg.MIN_PUNC,
                                                 Pg.MIN_PUNC + Pg.MIN_PUNC)
    punctuation_count = get_others_count(punctuation_template, Pg.MIN_PUNC,
                                         Pg.MIN_PUNC + Pg.MIN_PUNC,
                                         non_digit_temp, criteria_template)

    randomize_template = PREPEND + "Would you like shuffle the password (y/n): "
    randomize = None

    while True:
        randomize = get_user_input(randomize_template)
        if randomize == 'y' or randomize == 'Y':
            randomize = True
            break
        elif randomize == 'n' or randomize == 'N':
            randomize = False
            break
        else:
            print(PREPEND + INDICATOR + "Please enter only: y/n")

    generator_obj = Pg(tag, uppercase_count, lowercase_count,
                       digits_count, punctuation_count)
    tuple_ = generator_obj.generate_password(randomize)

    print(DASHES)
    print(PREPEND + "Password generation is completed!")
    print(DASHES)
    print(PREPEND + "Tag: {}".format(tuple_[0]))
    print(PREPEND + "Password: {}".format(tuple_[1]))
    print(PREPEND + "Hashed password: {}".format(tuple_[2]))
    print(INDICATOR + "Hash value has been added to the password storage.")

    write_to_file(tuple_[0], tuple_[2])


def generate_hash():
    """Handle the scenario when a user wants to generate a hash value of their
    own password which will be provided by the user and user password must be
    at least 1 or more characters long.

    Returns:
        None
    """

    template = PREPEND + "Please enter your password: "
    user_input = None

    while True:
        user_input = get_user_input(template)
        if len(user_input) < 1:
            print(PREPEND + INDICATOR +
                  "Please enter a password greater than 0")
        else:
            break

    hash_ = Pg.apply_hash(user_input)

    print(DASHES)
    print(PREPEND + "A hash value has been generated from your given password.")
    print(PREPEND + "Hash password: {}".format(hash_))
    print(INDICATOR + "RPG does not store hash value of user entered password.")


def generate_report():
    """Reads the password storage file and generates a reports on the
    followings: Total tags, total unique tags, total hashed passwords, total
    unique hashed passwords.

    Returns:
        None
    """

    if not os.path.exists(os.path.join(os.path.curdir, PASSWORD_STORAGE)):
        print(INDICATOR + "{} file is not in the current directory."
              .format(PASSWORD_STORAGE))
        print(INDICATOR + "Creating the file for you now ...")

        open(PASSWORD_STORAGE, "a+").close()

        if os.path.exists(os.path.join(os.path.curdir, PASSWORD_STORAGE)):
            print(INDICATOR + "file: {} has been created in the current "
                              "directory.".format(PASSWORD_STORAGE))
        return

    file_obj = open(PASSWORD_STORAGE, 'r')
    content = file_obj.readlines()
    file_obj.close()

    filtered_content = [line.strip()
                        for line in content
                        if len(line.strip()) >= 1]

    if len(filtered_content) == 0:
        print(INDICATOR + "Nothing to report as password storage is empty.")
        return

    report_dict = dict()

    for line in filtered_content:
        parts = line.strip().split(DELIMITER)
        try:
            hashes = report_dict[parts[0].strip()]
            hashes.append(parts[1].strip())
            report_dict[parts[0].strip()] = hashes
        except KeyError:
            hashes = [parts[1].strip()]
            report_dict[parts[0].strip()] = hashes

    total_tags, total_hashes, total_unique_hashes = 0, 0, 0
    for value in report_dict.values():
        total_tags += len(value)
        total_hashes += len(value)
        total_unique_hashes += len(set(value))

    print(PREPEND + "Total tags: {}".format(total_tags))
    print(PREPEND + "Total unique tags: {}".format(len(report_dict.keys())))
    print(PREPEND + "Total hashes: {}".format(total_hashes))
    print(PREPEND + "Total unique hashes: {}".format(total_unique_hashes))

    for key in report_dict.keys():
        values = report_dict[key]
        for value in values:
            print(PREPEND + "Key: {}, Hash: {}".format(key, value))


def main_menu():
    """This function acts as a menu and asks for a user input and finally
    takes action based upon the user input. User input must be integer
    otherwise appropriate error message is displayed.

    Returns:
        None
    """

    while True:
        print(DASHES)
        print("1) Generate a random password.")
        print("2) Generate hash value of your own password.")
        print("3) Generate and print a report from the password storage.")
        print("4) Exit.")
        print(DASHES)

        user_input = get_user_input("Please enter 1/2/3/4: ")

        try:
            user_input = int(user_input)
            if user_input == 1:
                generate_password()
            elif user_input == 2:
                generate_hash()
            elif user_input == 3:
                generate_report()
            elif user_input == 4:
                print(DASHES)
                break
            else:
                print(INDICATOR
                      + "Invalid selection entered. Please try again.")
        except ValueError:
            print(INDICATOR + "Expected integer value but found: {}. "
                              "Please try again.".format(str(user_input)))
            continue
        except Exception as e:
            print(INDICATOR + "Error: {}. Please try again.".format(str(e)))
            continue
        else:
            continue


if __name__ == "__main__":

    try:
        main_menu()
    finally:
        print("Thank you for using RPG. "
              "I hope the experience was good, \U0001F642")
        print(DASHES)
