from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("solomon", "fumador") == "fumador;solomon"
    assert make_full_name("Gilraddo", "Ephraim") == "Ephraim;Gilraddo"
    
def test_extract_family_name():
    assert extract_family_name("solomon; fumador") == "solomon"
    assert extract_family_name("Gilraddo; Ephraim") == "Gilraddo"

def test_extract_given_name():
    assert extract_given_name("Gilraddo/ Ephraim") == "Ephraim"
    assert extract_given_name("solomon/ fumador") == "fumador"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])

