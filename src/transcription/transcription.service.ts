import { Injectable, Logger } from '@nestjs/common';
import { exec } from 'child_process';
import * as fs from 'fs';
import * as path from 'path';

@Injectable()
export class TranscriptionService {
  private readonly logger = new Logger(TranscriptionService.name);

  async transcribe(audioFilePath: string): Promise<string> {
    this.logger.log(`Starting transcription for file: ${audioFilePath}`);

    return new Promise((resolve, reject) => {
      exec(`docker run --rm -v ${path.resolve(audioFilePath)}:/app/audio.mp3 whisper-transcription`, (error, stdout, stderr) => {
        if (error) {
          this.logger.error(`Error: ${error.message}`);
          return reject('Error during transcription');
        }
        if (stderr) {
          this.logger.error(`Stderr: ${stderr}`);
          return reject('Error during transcription');
        }

        this.logger.log('Transcription completed successfully.');
        const transcriptionResult = fs.readFileSync('/path/to/transcription/result.txt', 'utf8');
        this.logger.log(`Transcription result: ${transcriptionResult}`);
        resolve(transcriptionResult);
      });
    });
  }
}
