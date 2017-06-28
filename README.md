# alexa-open-vodka

Sample Amazon Alexa app playing predetermined audio on launch.

## Deployment

1. Sign up to [AWS](https://aws.amazon.com/)
2. Create a new Lambda function
3. Enter the code from [main.py](main.py)
4. Sign up to [Amazon Management Console](https://aws.amazon.com/console/)
5. Set up your Alexa app using ARN from AWS.

### Audio requirements

The SSML `<audio />` component accepts audio satisfying these requirements.

- bitrate at 48kbps
- length <= 90 seconds
- MPEGv2 codec
- available on HTTPS with trusted SSL certificate

You may use [FFmpeg](https://www.ffmpeg.org/) for conversions.

`ffmpeg -y -i input.mp3 -ar 16000 -ab 48k -codec:a libmp3lame -ac 1 output.mp3`

You may use Amazon S3 bucket for hosting.
