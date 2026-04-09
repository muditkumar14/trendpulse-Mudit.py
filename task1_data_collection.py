{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/muditkumar14/trendpulse-Mudit.py/blob/main/task1_data_collection.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "DRp3KRCocipF"
      },
      "outputs": [],
      "source": [
        "import requests\n",
        "import json\n",
        "import time"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hec0VsWxdUq"
      },
      "source": [
        "categories = {\n",
        "    'technology': ['AI', 'software', 'tech', 'code', 'computer', 'data', 'cloud', 'API', 'GPU', 'LLM'],\n",
        "    'worldnews': ['war', 'government', 'country', 'president', 'election', 'climate', 'attack', 'global'],\n",
        "    'sports': ['NFL', 'NBA', 'FIFA', 'sport', 'game', 'team', 'player', 'league', 'championship'],\n",
        "    'science': ['research', 'study', 'space', 'physics', 'biology', 'discovery', 'NASA', 'genome'],\n",
        "    'entertainment': ['movie', 'film', 'music', 'Netflix', 'game', 'book', 'show', 'award', 'streaming']\n",
        "} # Defining categories"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Task 1- Make the API Calls"
      ],
      "metadata": {
        "id": "e9XkMLkY6Stv"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OGKOrVzhdubc",
        "outputId": "5ab5fb1a-0a16-409b-951f-adaff67f7c68"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "fetched 500 stories\n",
            "First 5 IDs:[47697870, 47702196, 47702647, 47700388, 47691730]\n"
          ]
        }
      ],
      "source": [
        "headers = {\"User-Agent\": \"TrendPulse/1.0\"} # Define headers\n",
        "url='https://hacker-news.firebaseio.com/v0/topstories.json' # API\n",
        "try:\n",
        "  response=requests.get(url=url,headers=headers) # Make an HTTP GET request to the API\n",
        "  response.raise_for_status()\n",
        "  story=response.json()[:500]\n",
        "  print(f\"fetched {len(story)} stories\")\n",
        "  print(f\"First 5 IDs:{story[:5]}\")\n",
        "except requests.exceptions.RequestException as e:\n",
        "  print(f\"Failed to fetch top stories: {e}\") # Handling exceptions\n",
        "  exit()\n",
        "except json.JSONDecodeError as e:\n",
        "  print(f\"Failed to decode JSON response: {e}\") # Handle JSON decoding errors\n",
        "  exit()"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Task 2- Extract the Fields"
      ],
      "metadata": {
        "id": "aIt5IWP_6Vpq"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6tq3vrvIiq3V",
        "outputId": "f89c1332-2087-4645-be46-015a7e3f3bbc"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Fetched story 47702196 = technology\n",
            "Fetched story 47702647 = entertainment\n",
            "Fetched story 47663743 = sports\n",
            "Fetched story 47701233 = technology\n",
            "Fetched story 47695012 = technology\n",
            "Fetched story 47687273 = technology\n",
            "Fetched story 47692043 = worldnews\n",
            "Fetched story 47689174 = technology\n",
            "Fetched story 47666398 = entertainment\n",
            "Fetched story 47696035 = technology\n",
            "Fetched story 47700084 = technology\n",
            "Fetched story 47699814 = technology\n",
            "Fetched story 47676561 = entertainment\n",
            "Fetched story 47689237 = technology\n",
            "Fetched story 47693679 = technology\n",
            "Fetched story 47696562 = entertainment\n",
            "Fetched story 47694036 = entertainment\n",
            "Fetched story 47656518 = technology\n",
            "Fetched story 47701971 = technology\n",
            "Fetched story 47679121 = technology\n",
            "Fetched story 47700972 = technology\n",
            "Fetched story 47698067 = technology\n",
            "Fetched story 47674606 = technology\n",
            "Fetched story 47690797 = entertainment\n",
            "Fetched story 47689319 = technology\n",
            "Fetched story 47692661 = technology\n",
            "Fetched story 47689165 = sports\n",
            "Fetched story 47685945 = technology\n",
            "Fetched story 47661038 = entertainment\n",
            "Fetched story 47657204 = entertainment\n",
            "Fetched story 47624572 = technology\n",
            "Fetched story 47699090 = technology\n",
            "Fetched story 47677853 = worldnews\n",
            "Fetched story 47622717 = science\n",
            "Fetched story 47672295 = technology\n",
            "Fetched story 47673360 = entertainment\n",
            "Fetched story 47656682 = worldnews\n",
            "Fetched story 47696558 = technology\n",
            "Fetched story 47699105 = technology\n",
            "Fetched story 47664836 = technology\n",
            "Category 'technology' complete. Sleeping 2 seconds\n",
            "\n",
            "Fetched story 47680124 = worldnews\n",
            "Fetched story 47681112 = entertainment\n",
            "Fetched story 47697679 = entertainment\n",
            "Fetched story 47676557 = worldnews\n",
            "Fetched story 47680309 = entertainment\n",
            "Fetched story 47691174 = entertainment\n",
            "Fetched story 47654629 = sports\n",
            "Fetched story 47627217 = science\n",
            "Fetched story 47693407 = entertainment\n",
            "Fetched story 47672778 = sports\n",
            "Fetched story 47670981 = worldnews\n",
            "Fetched story 47674027 = entertainment\n",
            "Fetched story 47666024 = entertainment\n",
            "Fetched story 47636579 = entertainment\n",
            "Fetched story 47673880 = entertainment\n",
            "Fetched story 47664186 = sports\n",
            "Fetched story 47660954 = worldnews\n",
            "Fetched story 47637828 = entertainment\n",
            "Fetched story 47673394 = entertainment\n",
            "Fetched story 47676044 = entertainment\n",
            "Fetched story 47656501 = sports\n",
            "Fetched story 47629021 = worldnews\n",
            "Fetched story 47695616 = entertainment\n",
            "Fetched story 47662945 = worldnews\n",
            "Fetched story 47665685 = entertainment\n",
            "Fetched story 47660853 = entertainment\n",
            "Fetched story 47650502 = science\n",
            "Fetched story 47655392 = entertainment\n",
            "Category 'entertainment' complete. Sleeping 2 seconds\n",
            "\n",
            "Fetched story 47637377 = sports\n",
            "Fetched story 47665207 = science\n",
            "Fetched story 47647788 = worldnews\n",
            "Fetched story 47683613 = worldnews\n",
            "Fetched story 47677952 = worldnews\n",
            "Fetched story 47690049 = worldnews\n",
            "Fetched story 47656303 = science\n",
            "Fetched story 47693799 = worldnews\n",
            "Fetched story 47697980 = worldnews\n",
            "Fetched story 47692291 = worldnews\n",
            "Fetched story 47685704 = sports\n",
            "Fetched story 47691409 = science\n",
            "Fetched story 47648404 = science\n",
            "Fetched story 47629485 = science\n",
            "Fetched story 47694522 = science\n",
            "Fetched story 47639727 = sports\n",
            "Fetched story 47681453 = sports\n",
            "Fetched story 47633676 = sports\n",
            "Fetched story 47691869 = sports\n",
            "Fetched story 47686058 = worldnews\n",
            "Fetched story 47644726 = sports\n",
            "Fetched story 47672190 = sports\n",
            "Fetched story 47667008 = sports\n",
            "\n",
            " API calls complete!\n"
          ]
        }
      ],
      "source": [
        "category_counts = {cat: 0 for cat in categories} # Initialize a dictionary to keep track of collected stories per category\n",
        "collected_stories = []\n",
        "\n",
        "for s in story:\n",
        "  try:\n",
        "    story_url = f'https://hacker-news.firebaseio.com/v0/item/{s}.json' #  URL for fetching individual story details\n",
        "    story_response = requests.get(story_url, headers=headers) # Make an HTTP GET request for the story\n",
        "    story_response.raise_for_status() # Raise an HTTP Error\n",
        "    story_data = story_response.json() # Parse the JSON response\n",
        "    title = story_data.get('title', '').lower()\n",
        "    category = None\n",
        "\n",
        "    for cat, keywords in categories.items():\n",
        "        if any(keyword.lower() in title for keyword in keywords): # Check if any keyword is present in the story title\n",
        "            category = cat\n",
        "            break\n",
        "\n",
        "    if category and category_counts[category] < 25:\n",
        "        category_counts[category] += 1\n",
        "\n",
        "        story_entry = {\n",
        "            \"post_id\": s,\n",
        "            \"title\": story_data.get(\"title\", \"\"),\n",
        "            \"category\": category,\n",
        "            \"score\": story_data.get(\"score\", 0),\n",
        "            \"num_comments\": story_data.get(\"descendants\", 0),\n",
        "            \"author\": story_data.get(\"by\", \"unknown\"),\n",
        "            \"collected_at\": time.strftime(\"%Y-%m-%d %H:%M:%S\") # Record the time of collection\n",
        "        }\n",
        "        collected_stories.append(story_entry) # Add the formatted story data to our list\n",
        "\n",
        "        print(f\"Fetched story {s} = {category}\") # Print a confirmation message\n",
        "\n",
        "        if category_counts[category] == 25:\n",
        "            print(f\"Category '{category}' complete. Sleeping 2 seconds\\n\")\n",
        "            time.sleep(2)\n",
        "\n",
        "  except requests.exceptions.RequestException as e:\n",
        "      print(f\" Failed to fetch story {s}: {e}\") # Handle errors\n",
        "      continue\n",
        "  except json.JSONDecodeError as e:\n",
        "      print(f\" Failed to decode JSON for story {s}: {e}\") # Handle JSON decoding error\n",
        "      continue\n",
        "\n",
        "print(\"\\n API calls complete!\") # Indicate that all API calls have finished"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Task 3- Save to a JSON File"
      ],
      "metadata": {
        "id": "9DAqK3zJ7Rin"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "sZWxSDuwltmY",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "af07a9b1-346c-4f17-cfcb-f4c9576fefa6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collected 91 stories. Saved to data/trends_20240406.json\n"
          ]
        }
      ],
      "source": [
        "import os\n",
        "\n",
        "os.makedirs(\"data\", exist_ok=True) # Create a directory named 'data' if it doesn't already exist\n",
        "with open(\"data/trends_20240406.json\", 'w') as f: # Open a JSON file\n",
        "    json.dump(collected_stories, f, indent=2)\n",
        "print(f\"Collected {len(collected_stories)} stories. Saved to data/trends_20240406.json\") # Confirm saving and show the number of stories saved"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOeyYsY1ri+tC9YrOukdFgd",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}