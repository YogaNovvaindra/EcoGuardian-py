from flask import Blueprint, jsonify, request
from exponen.forecast import get_forecast
from exponen.clean_forecast import get_clean_forecast

# from exponen.pm25 import get_forecast_pm25
from ispu.ispu_main import get_ispu
from output.display import get_display
from output.mean import get_mean


bp = Blueprint("main", __name__)


@bp.route("/forecast", methods=["GET"])
def forecast():
    forecast = get_forecast()
    return jsonify({"Triple Exponential Smoothing Forecast": forecast})


@bp.route("/clean_forecast", methods=["GET"])
def clean_forecast():
    clean_forecast = get_clean_forecast()
    return jsonify({"Clean Forecast": clean_forecast})


# @bp.route('/forecast_pm25', methods=['GET'])
# def forecast_pm25():
#     # Get the 'esp_id' parameter from the query string
#     esp_id = request.args.get('esp_id')

#     if esp_id is None:
#         return jsonify({"error": "Missing 'esp_id' parameter"}), 400

#     # Use the 'esp_id' in your get_forecast_pm25 function
#     forecast_pm25 = get_forecast_pm25(esp_id)
#     return jsonify({"Triple Exponential Smoothing Forecast": forecast_pm25})


@bp.route("/ispu", methods=["GET"])
def get_ispu_co2_endpoint():
    # Get the 'esp_id' parameter from the query string

    # Call the get_ispu_co function to calculate the result
    ispu_result = get_ispu()
    return jsonify({"Result ISPU": ispu_result})


@bp.route("/display", methods=["GET"])
def get_display_endpoint():
    # Call the get_display function to calculate the result
    overall_avg_temperature, overall_avg_humidity, overall_avg_polution = get_display()
    return jsonify(
        {
            "Temperature": overall_avg_temperature,
            "Humidity": overall_avg_humidity,
            "Polution": overall_avg_polution,
        }
    )


@bp.route("/mean", methods=["GET"])
def get_mean_endpoint():
    # Call the get_mean function to calculate the result
    result = get_mean()
    return jsonify({"Result": result})
