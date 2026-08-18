# tests/test_my_first_test.py

from user_scanner.core.result import Result, Status

# Test 1: Prüfe Result.taken()
def test_result_taken():
    result = Result.taken()
    assert result.status == Status.TAKEN
    assert result.is_found() == True

# Test 2: Prüfe Result.available()
def test_result_available():
    result = Result.available()
    assert result.status == Status.AVAILABLE
    assert result.is_found() == False

# Test 3: Prüfe Result.error()
def test_result_error():
    result = Result.error("Something went wrong")
    assert result.status == Status.ERROR
    assert result.is_found() == False

# Test 4: Prüfe mit Username
def test_result_with_username():
    result = Result.taken(username="alice")
    assert result.username == "alice"
    assert result.is_found() == True

# Test 5: Prüfe Update-Funktion
def test_result_update():
    result = Result.available()
    result.update(username="bob", site_name="GitHub")
    
    assert result.username == "bob"
    assert result.site_name == "GitHub"
    
def test_result_status_labels():
    """Prüfe ob Status-Labels richtig angezeigt werden"""
    taken = Result.taken()
    available = Result.available()
    error = Result.error()
    
    # Für Username (is_email=False)
    assert str(taken) == "Found"
    assert str(available) == "Not Found"
    assert str(error) == "Error"
