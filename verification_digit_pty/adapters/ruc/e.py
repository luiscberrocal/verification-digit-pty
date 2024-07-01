from typing import List

from verification_digit_pty.exceptions import VerificationDigitError
from verification_digit_pty.plugins import register_plugin


@register_plugin
def e_adapter(ruc_parts: List[str]) -> str:
    try:
        ructb = '0' * (4 - len(ruc_parts[1])) + '0000005' + '00' + '50' + '0' * (3 - len(ruc_parts[1])) + ruc_parts[
            1] + '0' * (5 - len(ruc_parts[2])) + \
                ruc_parts[2]
    except IndexError:
        raise VerificationDigitError('Invalid RUC') from None
    return ructb
