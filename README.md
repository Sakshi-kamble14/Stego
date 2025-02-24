# Secure Data Hiding in Images Using Steganography

## Project Description
This project implements image steganography to securely hide encrypted messages within images. By combining AES encryption with Least Significant Bit (LSB) modification, it ensures secure and undetectable communication.

## Features
- **AES Encryption:** Adds an extra layer of security before hiding data.
- **LSB Steganography:** Ensures minimal image distortion.
- **Steganalysis Resistance:** Uses AI techniques to counter detection attacks.
- **Multi-Format Support:** Works with various image formats like PNG and JPEG.
- **Cloud Security:** Enables encrypted cloud-based data sharing.
- **Blockchain Integration:** Ensures tamper-proof data transmission.
- **Audio/Video Steganography (Future Scope):** Extendable to other media types.

## Installation
### Prerequisites
- Python 3.x
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)
- Cryptography (`pip install cryptography`)

### Steps
1. Clone the repository:
   ```bash
   git clone <https://github.com/Sakshi-kamble14/Stego/blob/main/stego.py)>
   
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python steganography.py
   ```

## Usage
1. Run the script and provide a secret message & passcode.
2. The message will be encrypted and embedded into an image.
3. To retrieve the message, enter the correct passcode for decryption.

## Technologies Used
- **Programming Language:** Python
- **Libraries:** OpenCV, NumPy, Cryptography
- **Encryption Method:** AES (Advanced Encryption Standard)
- **Steganography Technique:** Least Significant Bit (LSB) modification

## End Users
- Individuals and organizations requiring secure data transmission.
- Journalists, whistleblowers, and activists communicating sensitive information.
- Government and defense agencies for covert communication.
- Cybersecurity professionals and ethical hackers studying secure data transmission methods.

## Future Scope
- **AI-based Detection Resistance:** Improve steganalysis resistance.
- **Mobile & Web App:** Develop a user-friendly application.
- **Blockchain Integration:** Secure verification of hidden messages.
- **Multi-Media Support:** Extend steganography to audio and video.

## Contributors
- Sakshi Shivaji Kamble
- Vignesh M Sir

## License
This project is licensed under the MIT License.

## GitHub Repository
[GitHub Repository Link](https://github.com/Sakshi-kamble14/Stego/blob/main/stego.py)
