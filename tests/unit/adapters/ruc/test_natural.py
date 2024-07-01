from verification_digit_pty.adapters.ruc.natural import e_adapter, e_adapter_new


def test_natural_e_adapter():
    cedula ='E-12-342'
    print(e_adapter(cedula))

    expected_value = '000000005005001200342'
    assert e_adapter(cedula) == expected_value
    assert len(e_adapter(cedula)) == 21

    new_value = e_adapter_new(cedula)
    assert new_value == expected_value
    assert len(new_value) == 21
