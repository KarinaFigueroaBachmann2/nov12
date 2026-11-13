from supabase import create_client

url = "https://apkqaalyrgzblzdvdrmj.supabase.co"
key = "sb_secret_92z0vL4zFo6LizHWdeq02g_Rbf5D1-4"

supabase = create_client(url, key)

try:
    respuesta = (
        supabase
        .table("vehiculos")
        .select("*")
        .limit(1)
        .execute()
    )

    print("CONEXION OK")
    print(respuesta)

except Exception as e:
    print("ERROR:")
    print(e)
