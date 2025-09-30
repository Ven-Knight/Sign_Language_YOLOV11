# ─────────────────────────────────────────────────────────────
# Logger Setup — Timestamped, Root-Relative, Audit-Ready
# ─────────────────────────────────────────────────────────────

import logging
import os
from   datetime  import datetime
from   from_root import from_root  # resolves project root path


LOG_FILE      = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # Generate unique log filename

log_dir       = os.path.join(from_root(), 'log')
os.makedirs(log_dir, exist_ok=True)                                    # Create log directory if missing

LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)                        # Full path to log file

logging.basicConfig(
                        filename = LOG_FILE_PATH,
                        format   = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
                        level    = logging.INFO
                    )                                                  # Configure logging: timestamp, module name, level, message