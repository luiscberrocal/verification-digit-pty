from verification_digit_pty.enums import NaturalRUCLetter, Province
from verification_digit_pty.exceptions import VerificationDigitError
from verification_digit_pty.plugins import register_plugin


def e_adapter_old(ruc: str) -> str:
    ruc_parts = ruc.split('-')
    try:
        ructb = '0' * (4 - len(ruc_parts[1])) + '0000005' + '00' + '50' + '0' * (3 - len(ruc_parts[1])) + ruc_parts[
            1] + '0' * (5 - len(ruc_parts[2])) + \
                ruc_parts[2]
    except IndexError:
        raise VerificationDigitError('Invalid RUC') from None
    return ructb


@register_plugin
def e_adapter(ruc: str) -> str:
    ruc_parts = ruc.split('-')
    letter = NaturalRUCLetter.from_code(ruc_parts[0])
    folio_imagen = ruc_parts[1]
    asiento_ficha = ruc_parts[2]
    max_folio_len = 4
    asiento_max_len = 9

    if 0 < len(folio_imagen) < max_folio_len:
        if len(asiento_ficha) == 6 and letter in (NaturalRUCLetter.E, NaturalRUCLetter.N):
            ructb = ("5" + "00" + letter.code.ljust(2, "0") +
                     folio_imagen.zfill(3) + asiento_ficha).zfill(20)
        else:
            ructb = ("5" + "00" + letter.code.ljust(2, "0") +
                     folio_imagen.zfill(3) + asiento_ficha[:5].zfill(5)).zfill(20)
    else:
        if len(asiento_ficha) == 6 and letter in (NaturalRUCLetter.E, NaturalRUCLetter.N):
            ructb = ("5" + letter.validation_code + letter.code.ljust(2, "0") +
                     folio_imagen.zfill(4) + asiento_ficha).zfill(20)
        else:
            ructb = ("5" + letter.validation_code + letter.code +
                     folio_imagen.zfill(4) + asiento_ficha[:5].zfill(5)).zfill(20)
    return ructb


def n_adapter(ruc: str) -> str:
    return e_adapter(ruc)


def av_adapter(ruc: str) -> str:
    ruc_parts = ruc.split('-')
    letter = NaturalRUCLetter.from_part(ruc_parts[0])
    folio_imagen = ruc_parts[1]
    asiento_ficha = ruc_parts[2]
    max_folio_len = 4
    asiento_max_len = 9
    province = Province.from_part(ruc_parts[0])
    if 0 < len(folio_imagen) < max_folio_len:
        ructb = ("5" + province.code.zfill(2) + letter.code + folio_imagen.zfill(3) +
                 asiento_ficha[:5].zfill(5)).zfill(20)
    else:
        ructb = ("5" + letter.validation_code + folio_imagen.zfill(4) +
                 asiento_ficha[:5].zfill(5)).zfill(20)
    return ructb


def pi_adapter(ruc: str) -> str:
    return av_adapter(ruc)


def pe_adapter(ruc: str) -> str:
    return e_adapter(ruc)
