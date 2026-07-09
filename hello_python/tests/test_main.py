from hello_python.main import main


def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Привет, мир!\n"
