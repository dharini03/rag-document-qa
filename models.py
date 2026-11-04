# from django.db import models

# class UploadedFile(models.Model):
#     file = models.FileField(upload_to='documents/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to="documents/")

class TextChunk(models.Model):
    file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    chunk_text = models.TextField()
    chunk_index = models.IntegerField()

class Embedding(models.Model):
    chunk = models.OneToOneField(TextChunk, on_delete=models.CASCADE)
    vector = models.BinaryField()  # store np.array as bytes if needed
