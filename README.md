# normalizer_usps

**normalizer_usps** is a Python library for normalizing US addresses by abbreviating street types and secondary address designations according to USPS standards.

## Features

- **Street Type Abbreviation**: Converts street types like "Street" to "ST", "Avenue" to "AVE", etc.
- **Secondary Address Abbreviation**: Abbreviates secondary address units like "Apartment" to "APT", "Suite" to "STE".
- **Easy Integration**: Designed to work seamlessly with Pandas Series for batch processing.

## Installation

Install the package using pip:

```bash
pip install normalizer_usps
```

## Usage

import pandas as pd
from normalizer_usps.normalizer import abbreviate_address_series, street_type_abbreviations, secondary_address_abbreviations

### Sample address data
addresses = pd.Series([
    '123 Happy Street',
    '456 Elm Avenue',
    '789 Oak Boulevard',
    '101 Maple Apartment'
])

###  Normalize street types
normalized_addresses = abbreviate_address_series(addresses, street_type_abbreviations)
print(normalized_addresses)

### Normalize secondary address units
normalized_addresses = abbreviate_address_series(addresses, secondary_address_abbreviations)
print(normalized_addresses)

```bash
0     123 HAPPY ST
1       456 ELM AVE
2    789 OAK BLVD
3    101 MAPLE APT
dtype: object

```

## Data Files
The package includes two JSON files containing abbreviation mappings:

street_type_abbreviations.json
secondary_address_abbreviations.json
Contributing
Contributions are welcome! Please open an issue or submit a pull request on GitHub.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Author
Larissa
larissabeatrizlima@outlook.com
