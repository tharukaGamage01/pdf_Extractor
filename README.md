# PDF Extractor

A powerful Python application that extracts structured hotel information from PDF rate sheets using AI-powered text processing and stores the data in Supabase.

## ✨ Features

- **PDF Text Extraction**: Efficiently extracts text from hotel rate sheet PDFs using `pdfplumber`
- **AI-Powered Parsing**: Uses OpenAI's GPT-4 to intelligently extract structured data from unstructured text
- **Smart Validation**: Validates extracted text quality before processing
- **Database Storage**: Automatically stores processed data in Supabase
- **Fallback Processing**: Gracefully handles different text extraction scenarios
- **Comprehensive Data**: Extracts hotel details, rates, policies, and more

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   PDF Input     │ -> │  Text Extractor │ -> │   Validator     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Supabase DB   │ <- │  Data Processor │ <- │  GPT-4 Engine   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📋 Data Structure

The parser extracts the following information:

- **Hotel Information**: Name, location, contact details
- **Rate Seasons**: Seasonal pricing with start/end dates
- **Room Categories**: Room types, descriptions, and sizes
- **Meal Plans**: Available plans with descriptions and rates
- **Policies**: Check-in/out times, child policy, cancellation policy
- **Metadata**: Processing method, validation score, text length

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- OpenAI API key
- Supabase account and API credentials

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tharukaGamage01/pdf_Extractor.git
   cd pdf_Extractor
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   SUPABASE_URL=your_supabase_url_here
   SUPABASE_KEY=your_supabase_key_here
   ```

### Usage

1. **Update the PDF path** in `main.py`:
   ```python
   PDF_PATH = "/path/to/your/hotel/rate/sheet.pdf"
   ```

2. **Run the parser**:
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
hotel_pdf_parser/
├── main.py              # Main application entry point
├── parser.py            # PDF text extraction logic
├── validator.py         # Text validation functions
├── gpt_extractor.py     # GPT-4 integration for data extraction
├── supabase_client.py   # Database operations
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not tracked)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |
| `SUPABASE_URL` | Your Supabase project URL | Yes |
| `SUPABASE_KEY` | Your Supabase API key | Yes |

### Supabase Table Schema

The application expects a table named `hotels_rate_data` with the following structure:

```sql
CREATE TABLE hotels_rate_data (
    id UUID PRIMARY KEY,
    pdf_filename TEXT,
    hotel_name TEXT,
    hotel_location TEXT,
    hotel_contact TEXT,
    rate_seasons JSONB,
    room_categories JSONB,
    meal_plans JSONB,
    check_in_time TEXT,
    check_out_time TEXT,
    child_policy TEXT,
    cancellation_policy TEXT,
    processing_method TEXT,
    validation_score INTEGER,
    extracted_text_length INTEGER,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE
);
```

## 🧪 How It Works

1. **Text Extraction**: The `parser.py` module uses `pdfplumber` to extract raw text from PDF files
2. **Validation**: The `validator.py` checks if the extracted text contains essential hotel-related keywords
3. **AI Processing**: If validation passes, or as a fallback, `gpt_extractor.py` uses GPT-4 to structure the data
4. **Data Storage**: Processed data is stored in Supabase via `supabase_client.py`

## 🔍 Validation Logic

The system validates extracted text by checking for key terms:
- "room" - Room-related information
- "rate" - Pricing information
- "season" - Seasonal data
- "check-in" - Check-in policies
- "child" - Child policies

Validation score = (number of keywords found) × 20

## 🤖 GPT-4 Integration

The application uses OpenAI's GPT-4 to:
- Parse unstructured text into structured JSON
- Extract complex hotel information
- Handle various PDF formats and layouts
- Provide consistent data structure

## 🛠️ Dependencies

- **pdfplumber**: PDF text extraction
- **openai**: GPT-4 API integration
- **python-dotenv**: Environment variable management
- **supabase**: Database operations

## 🚨 Error Handling

The application includes robust error handling for:
- Invalid PDF paths
- JSON parsing errors from GPT-4
- Database connection issues
- API rate limits and failures

## 📈 Future Enhancements

- [ ] Support for multiple PDF formats
- [ ] Batch processing capabilities
- [ ] Web interface for file uploads
- [ ] Advanced validation rules
- [ ] Export functionality (CSV, Excel)
- [ ] Real-time processing status

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for providing the GPT-4 API
- Supabase for the database infrastructure
- The `pdfplumber` library for PDF processing capabilities

---

**Made by [Tharuka Gamage](https://github.com/tharukaGamage01)**
