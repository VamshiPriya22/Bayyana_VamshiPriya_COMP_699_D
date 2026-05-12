from .models import Job


class JobService:

    @staticmethod
    def create_job(user, form):
        job = form.save(commit=False)
        job.user = user
        job.save()
        return job

    @staticmethod
    def update_job(job, form):
        job.job_name = form.cleaned_data['job_name']
        job.pay_rate = form.cleaned_data['pay_rate']
        job.location = form.cleaned_data['location']
        job.save()

    @staticmethod
    def delete_job(job):
        job.delete()

    @staticmethod
    def get_user_jobs(user):
        return Job.objects.filter(user=user)