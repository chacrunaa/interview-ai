import { Controller, Post, UploadedFile, UseInterceptors, Res } from '@nestjs/common';
import { FileInterceptor } from '@nestjs/platform-express';
import { Response } from 'express';
import { TranscriptionService } from './transcription.service';
import * as path from 'path';

@Controller('transcribe')
export class TranscriptionController {
  constructor(private readonly transcriptionService: TranscriptionService) {}

  @Post()
  @UseInterceptors(FileInterceptor('file', {
    dest: './uploads', // Папка, куда будут сохраняться загруженные файлы
  }))
  async transcribe(@UploadedFile() file: Express.Multer.File, @Res() res: Response) {
    const audioFilePath = path.resolve('./uploads', file.filename); // Путь к загруженному файлу
    try {
      const result = await this.transcriptionService.transcribe(audioFilePath);
      res.send(result);
    } catch (error) {
      res.status(500).send('Error during transcription');
    }
  }
}
