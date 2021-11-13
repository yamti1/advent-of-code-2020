from .part_1 import (
    Policy,
    load_policies_and_passwords, 
    PASSWORDS_FILENAME, 
    get_valid_passwords,
)


class UpdatedPolicy(Policy):
    def is_password_matching(self, password: str) -> bool:
        candidates = password[self.min_count - 1], password[self.max_count - 1]
        return candidates.count(self.letter) == 1


def main():
    policies_and_passwords = load_policies_and_passwords(PASSWORDS_FILENAME, policy_cls=UpdatedPolicy)
    valid_passwords = get_valid_passwords(policies_and_passwords)
    print(len(valid_passwords))
    

if __name__ == "__main__":
    main()