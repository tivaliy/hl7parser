# hl7parser

Library for parsing HL7 messages into various formats.

## Quickstart

1. Clone the repository:

        $ git clone git@bitbucket.org:e2fdev/hl7parser.git

2. Install the package:

        $ pip install .

3. Use as a package:

    ```python
    from hl7parser import HL7MessageParser

    message = """
    MSH|^~\&|FROM_APP|FROM_FACILITY|TO_APP|TO_FACILITY|20180101000000||ADT^A01|20180101000000|P|2.5|
    EVN|A01|20110613083617|
    PID|1|843125^^^^MRN|21004053^^^^MRN~2269030303^^^^ORGNMBR||SULLY^BRIAN||19611209|M|||123 MAIN ST^^CITY^STATE^12345|
    PV1||I|H73 RM1^1^^HIGHWAY 01 CLINIC||||5148^MARY QUINN|||||||||Y||||||||||||||||||||||||||||20180101000000|
    """

    HL7MessageParser.hl7_to_dict(message)
    ```

4. Use as a CLI application:

    ```sh
    $ hl7parser --help

    Options:
        -v, --version             Show the application's version and exit.
        --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
        --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
        --help                    Show this message and exit.

     Commands:
        convert  Converts an HL7 file into an appropriate format.

    $ hl7parser convert data/ORU/2022-09-05T10_22_37.hl7 --output 2022-09-05T10_22_37.json

      Invalid value for TN data
      a453e3488ac7a1a478ebfb6abeead801dd5ebc82 is not an HL7 valid NM value
      Invalid value for TN data
      da39a3ee5e6b4b0d3255bfef95601890afd80709 is not an HL7 valid NM value
      Invalid value for TN data
      da39a3ee5e6b4b0d3255bfef95601890afd80709 is not an HL7 valid NM value
    ```

## Setup Development Environment

1. Create a virtualenv:

        $ python3.9 -m venv <virtual_env_path>

2. Activate the virtualenv:

        $ source <virtual_env_path>/bin/activate

3. Prepare development environment:

* Install package dependencies:

        $ pip install -r requirements.txt

* Configure `pre-commit` hooks:

        $ pre-commit install

## Contributing

All changes in the project codebase *must* be done via Pull Requests.
