from verification_digit_pty.adapters.ruc.natural import e_adapter, e_adapter_old


def test_natural_e_adapter():
    """Error in calculating the rud format e_adapter returns 21 digits instead of 20"""
    cedula = 'E-12-342'
    print(e_adapter(cedula))

    expected_value = '000000005005001200342'
    assert e_adapter_old(cedula) == expected_value
    assert len(e_adapter(cedula)) == 20

    new_value = e_adapter(cedula)
    # assert new_value == expected_value
    assert len(new_value) == 20
