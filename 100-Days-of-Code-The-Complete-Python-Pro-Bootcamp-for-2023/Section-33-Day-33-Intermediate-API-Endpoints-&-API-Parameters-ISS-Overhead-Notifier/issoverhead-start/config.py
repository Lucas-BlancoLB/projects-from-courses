import smtplib
# OBJECTIVE: check if ISS is close by
class IsISSClose:
    def __init__(self, param, iss_pos, sun_info, current_time, login_info):
        self.my_Lat = param["lat"]
        self.my_lng = param["lng"]
        self.iss_lat = iss_pos[0]
        self.iss_lng = iss_pos[1]
        self.sunrise = sun_info[0]
        self.sunset = sun_info[1]
        self.time = current_time
        self.smtp_address = login_info[0]
        self.email = login_info[1]
        self.password = login_info[2]



    def is_iSS_close(self):
        if self.my_lng -5 <= self.iss_lng <= self.my_lng +5 and self.my_Lat -5 <= self.iss_lat <= self.my_Lat +5:
            if not self.sunrise < self.time <= self.sunset:
                with smtplib.SMTP(self.smtp_address, port=587) as server:
                    server.starttls()
                    server.login(user=self.email, password=self.password)
                    server.sendmail(from_addr=self.email, to_addrs=self.email, msg="Subject: Hey, look up\n\nISS is above you!")
                    return True
