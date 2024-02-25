from bson import ObjectId

class Job:
    def __init__(self, company, job_link, job_location, post_time, job_description, seniority_level, employment_type, industry, job_function, job_title):
        self._id = ObjectId() # unique id for job posting
        self.company = company # company name
        self.link = job_link # link to job posting
        self.location = job_location # job city, state
        self.post_time = post_time # date job was posted
        self.description = job_description # job description, requirements, qualifications, etc.
        self.seniority_level = seniority_level # entry, mid, senior, etc.
        self.employment_type = employment_type # full-time, part-time, contract, etc.
        self.industry = industry # industry of job posting
        self.job_function = job_function
        self.job_title = job_title

    