from argparse import ArgumentParser


def add_list_services_args(parser: ArgumentParser) -> ArgumentParser:
    return parser


def add_stop_all_args(parser: ArgumentParser) -> ArgumentParser:
    return parser


def add_stop_service_args(parser: ArgumentParser) -> ArgumentParser:
    parser.add_argument(
        "--pid",
        help="process id",
        dest="pid",
        type=int,
        required=True,
    )
    return parser


def add_start_service_args(parser: ArgumentParser) -> ArgumentParser:
    parser.add_argument(
        "--input",
        help="_description_",
        dest="input",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--output",
        help='_description_. Defaults to "config.py".',
        dest="output",
        type=str,
        default="config.py",
        required=False,
    )
    return parser


def add_to_code_args(parser: ArgumentParser) -> ArgumentParser:
    parser.add_argument(
        "--input",
        help="The path to the configuration file (YAML or JSON).",
        dest="input",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--output",
        help="The path to the output file where the generated",
        dest="output",
        type=str,
        default="config.py",
        required=False,
    )
    return parser


def setup_config2code_parser(parser: ArgumentParser) -> ArgumentParser:
    command_subparser = parser.add_subparsers(dest="command", title="command")
    to_code = command_subparser.add_parser(
        "to-code",
        help="Converts a configuration file to a Python dataclass and writes the code to a file.",
    )
    to_code = add_to_code_args(to_code)
    start_service = command_subparser.add_parser("start-service", help="_summary_")
    start_service = add_start_service_args(start_service)
    stop_service = command_subparser.add_parser(
        "stop-service", help="stop a particular service"
    )
    stop_service = add_stop_service_args(stop_service)
    stop_all = command_subparser.add_parser("stop-all", help="stop all services")
    stop_all = add_stop_all_args(stop_all)
    list_services = command_subparser.add_parser(
        "list-services", help="print currently running processes"
    )
    list_services = add_list_services_args(list_services)
    return parser


def setup_parser(parser: ArgumentParser) -> ArgumentParser:
    parser = setup_config2code_parser(parser)
    return parser
