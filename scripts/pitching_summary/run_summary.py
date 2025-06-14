#!/usr/bin/env python3

import argparse

from src.pitching_summary.data_processing import process_data

from src.pitching_summary.plotting_functions import (

    plot_pitch_breaks, plot_zone

)
 
def main():

    parser = argparse.ArgumentParser(

        description="Generate a pitching summary for a given pitcher and date range"

    )

    parser.add_argument("--first-name", required=True,

                        help="Pitcher's first name")

    parser.add_argument("--last-name", required=True,

                        help="Pitcher's last name")

    parser.add_argument("--start-date", required=True,

                        help="Start date (YYYY-MM-DD)")

    parser.add_argument("--end-date", required=True,

                        help="End date (YYYY-MM-DD)")

    args = parser.parse_args()
 
    df = process_data(args.first_name, args.last_name,

                      args.start_date, args.end_date)

    plot_pitch_breaks(df, args.first_name, args.last_name)

    plot_zone(df, args.first_name, args.last_name)
 
if __name__ == "__main__":

    main()

