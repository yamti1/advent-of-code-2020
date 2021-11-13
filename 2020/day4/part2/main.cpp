#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <map>
#include <array>
#include <list>
#include <regex>

const std::string PASSPORT_FILENAME = "../input.txt";

const std::map<std::string, std::regex> REQUIRED_FIELDS_TO_REGEX = {
    {"byr", std::regex("(19[2-9][0-9]|200[0-2])")},
    {"iyr", std::regex("(201[0-9]|2020)")},
    {"eyr", std::regex("(202[0-9]|2030)")},
    {"hgt", std::regex("((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)")},
    {"hcl", std::regex("#[0-9a-f]{6}")},
    {"ecl", std::regex("(amb|blu|brn|gry|grn|hzl|oth)")},
    {"pid", std::regex("[0-9]{9}")},
};

const int MAX_PASSPORT_LENGTH = 1000;
const char KEY_VALUE_DELIMITER = ':';
const char PAIR_DELIMITER = ' ';

using Passport = std::map<std::string, std::string>;

bool isValidPassport(const Passport& passport) {
    for (auto &&pair : REQUIRED_FIELDS_TO_REGEX)
    {
        const std::string& field = pair.first;
        const std::regex& regex = pair.second;

        if (passport.count(field) == 0)
        {
            return false;
        }
        if (!std::regex_match(passport.at(field), regex))
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
    std::string field, value;
    while (std::getline(stream, field, KEY_VALUE_DELIMITER))
    {
        std::getline(stream, value, PAIR_DELIMITER);
        result.insert({field, value});
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
        for (auto &&pair : passport)
        {
            std::cout << pair.first << ": " << pair.second << " ";
        }
        std::cout << (isValid ? "valid" : "invalid") << std::endl;
        
        counter += isValidPassport(passport);
        index += 1;
    }
    
    std::cout << counter << std::endl;
}
