{
    "DATETIME": {
        "call_str":
        "DateServiceROUND_DATE(AFFIRMED_MME_FPP_StringToTimeZone(DATETIME),5,\"D\")",
        "generate_temp": "False"
    },
    "INPUT_FILE_NAME": {
        "call_str": "delivery.Source_Name",
        "generate_temp": "False"
    },
    "DATETIME_FTP_COLLECTION": {
        "call_str":
        "AFFIRMED_VMCC_FPP_getDatetimeFtpCollection(delivery.Source_Name)",
        "generate_temp": "False"
    },
    "LOCAL_DATETIME": {
        "call_str": "AFFIRMED_VMCC_FPP_GetGMTTimeZone(DATETIME,{zone_name})",
        "generate_temp": "False"
    },
    "PERIOD": {
        "call_str": 300,
        "generate_temp": "True"
    }
}
