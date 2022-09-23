import json
import logging
import time
from dataclasses import asdict, dataclass

import click
import gpxpy
import gpxpy.gpx
import requests

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)


@dataclass(kw_only=True, repr=True)
class PointData:
    lon: float
    lat: float
    ele: float
    name: float


def post_point_data(point_data: PointData, host: str, port: str, topic: str):
    url = f"{host}:{port}/producer/{topic}"
    response = requests.post(url, json.dumps(asdict(point_data)))


@click.command()
@click.option("--file", help="GPX file path")
@click.option("--host", help="Host URL")
@click.option("--port", help="Producer API port")
def main(file, host, port):

    try:
        with open(file) as gpx_file:
            gpx_data = gpxpy.parse(gpx_file)
            for track in gpx_data.tracks:
                for segment in track.segments:
                    sleep_time = 0
                    prev_time = None
                    for point in segment.points:
                        if prev_time:
                            sleep_time = (point.time - prev_time).seconds
                        time.sleep(sleep_time)
                        prev_time = point.time
                        point = PointData(
                            lat=point.latitude,
                            lon=point.longitude,
                            ele=point.elevation,
                            name=gpx_file.name,
                        )
                        logging.info(msg=f"Sending point: {point}")
                        post_point_data(point, host, port, "stream")

    except FileNotFoundError as file_error:
        logging.exception(file_error)


if __name__ == "__main__":
    main()
