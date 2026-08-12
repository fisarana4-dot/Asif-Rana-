import os;k=os.getenv('GEMINI_API_KEY') or (os.path.exists('.env') and open('.env').read().split('"')[1]);print('STATUS: OK' if k else 'FAIL')
