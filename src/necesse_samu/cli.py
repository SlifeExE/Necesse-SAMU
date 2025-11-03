import argparse
import sys

from .config import load_config
from .updater import run_update


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Necesse Server and Mod Updater")
    parser.add_argument("--config", "-c", help="Path to config.json", default=None)
    args = parser.parse_args(argv)

    cfg = load_config(args.config)
    code = run_update(cfg)

    # Optional pause on exit (useful when double-clicking the EXE)
    try:
        if cfg.pause_on_exit:
            # Prefer msvcrt for any key on Windows, else fallback to Enter
            import msvcrt  # type: ignore
            print("\nPress any key to close...")
            msvcrt.getch()
        else:
            pass
    except Exception:
        try:
            input("\nPress Enter to close...")
        except Exception:
            pass

    return code


if __name__ == "__main__":
    sys.exit(main())
