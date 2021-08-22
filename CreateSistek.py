# --------------------------------------------------------------------------------------------------------------------------------------------
#     Author:   Kwabina A. Griffith
# Start Date:   July 26, 2021
#   End Date:   July 31, 2021
#   Modified:
#    Purpose:   Convert the Euronet embossing file to Sistek Format
# --------------------------------------------------------------------------------------------------------------------------------------------

import SistekIO
import SistekConversion

#  ----------
#  MAIN LOGIC |
#  ----------

euronet_data = SistekIO.read_euronet_file()
sistek_records = SistekConversion.convert_to_sistek(euronet_data)
SistekIO.write_sistek_file(sistek_records)
SistekIO.write_backup_file(sistek_records)