#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <set>
#include <array>
#include <list>


const std::string PASSPORT_FILENAME = "../input.txt";

const std::array<const std::string, 7> REQUIRED_FIELDS = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
};
const int MAX_PASSPORT_LENGTH = 1000;
const char KEY_VALUE_DELIMITER = ':';
const char PAIR_DELIMITER = ' ';

using Passport = std::set<std::string>;

bool isValidPassport(const Passport& passport) {
    for (auto &&field : REQUIRED_FIELDS)
    {
        if (!passport.count(field))
        {
            return false;
        }
    }
    return true;
}

std::list<std::string> loadPassportFile(const std::string& filename) {
    std::list<std::string> result;
    std::ifstream file(filename);

    std::string passport;
    std::string line;
    while (std::getline(file, line))
    {
        if (line == "")
        {
            result.push_back(passport);
            passport = "";
            continue;    
        }
        passport += line + PAIR_DELIMITER;        
    }

    if (passport != "") {
        result.push_back(passport);
    }

    file.close();
    return result;
}

Passport parsePassportLine(const std::string& line) {
    Passport result;
    std::stringstream stream(line);
    std::string field;
    while (std::getline(stream, field, KEY_VALUE_DELIMITER))
    {
        result.insert(field);
        // Get rid of the value of the field
        std::getline(stream, field, PAIR_DELIMITER);
    }
    return result;
}

int main() {
    int counter = 0;
    int index = 0;
    const auto passportLines = loadPassportFile(PASSPORT_FILENAME);
    for (auto &&passportLine : passportLines)
    {
        const auto passport = parsePassportLine(passportLine);
        
        const auto isValid = isValidPassport(passport);

        std::cout << index << ": ";
        for (auto &&field : passport)
        {
            std::cout << field << " ";
        }
        std::cout << (isValid ? "valid" : "invalid") << std::endl;
        
        counter += isValidPassport(passport);
        index += 1;
    }
    
    std::cout << counter << std::endl;
}
