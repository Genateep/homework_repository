from homework4.task03 import my_precious_logger


def test_my_precious_logger(capsys):
    my_precious_logger("OK")
    my_precious_logger("error: file not found")
    capture = capsys.readouterr()

    assert "OK" in capture.out
    assert "error: file not found" in capture.err
