from dataclasses import dataclass


PASSWORDS_FILENAME = "passwords.txt"
RANGE_SEPARATOR = "-"
POLICY_PASSWORD_SEPARATOR = ":"


@dataclass
class Policy:
    min_count: int
    max_count: int
    letter: str

    def is_password_matching(self, password: str) -> bool:
        count = password.count(self.letter)
        return self.min_count <= count <= self.max_count
    
    @classmethod
    def from_policy_line(cls, line: str) -> 'Policy':
        range, letter = line.split(" ")
        min_count, max_count = range.split(RANGE_SEPARATOR)
        return cls(int(min_count), int(max_count), letter)


def load_policies_and_passwords(passwords_filename: str, policy_cls: type = Policy):
    with open(passwords_filename, 'r') as f:
        return [
            (
                policy_cls.from_policy_line(line.split(POLICY_PASSWORD_SEPARATOR)[0]),
                line.split(POLICY_PASSWORD_SEPARATOR)[1].strip()
            ) 
            for line in f
        ]


def get_valid_passwords(policies_and_passwords):
    return [
        password for policy, password in policies_and_passwords 
        if policy.is_password_matching(password)
    ]


def main():
    policies_and_passwords = load_policies_and_passwords(PASSWORDS_FILENAME)
    valid_passwords = get_valid_passwords(policies_and_passwords)
    print(len(valid_passwords))
    

if __name__ == "__main__":
    main()
