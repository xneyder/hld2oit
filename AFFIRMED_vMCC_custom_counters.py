{
    "DATETIME": {
        "call_str":
        "DateServiceROUND_DATE(AFFIRMED_MME_FPP_StringToTimeZone(DATETIME),5,\"D\")"
    },
    "INPUT_FILE_NAME": {
        "call_str": "delivery.Source_Name"
    },
    "DATETIME_FTP_COLLECTION": {
        "call_str": "AFFIRMED_VMCC_FPP_getDatetimeFtpCollection(delivery.Source_Name)"
    },
    "LOCAL_DATETIME": {
        "call_str": "AFFIRMED_VMCC_FPP_GetGMTTimeZone(DATETIME,{zone_name})"
    },
    "PERIOD": {
        "call_str": 300,
        "generate_temp": "True"
    }
}
