#!/usr/bin/env python3
"""
Test script to verify all imports work correctly for Render deployment
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test all critical imports"""
    try:
        print("Testing imports...")
        
        # Test basic imports
        import asyncio
        print("✓ asyncio imported successfully")
        
        # Test third-party imports
        import pyrogram
        print("✓ pyrogram imported successfully")
        
        import pytgcalls
        print("✓ pytgcalls imported successfully")
        
        import motor
        print("✓ motor imported successfully")
        
        import yt_dlp
        print("✓ yt-dlp imported successfully")
        
        import spotipy
        print("✓ spotipy imported successfully")
        
        # Test local imports
        import config
        print("✓ config imported successfully")
        
        from AnonXMusic.logging import LOGGER
        print("✓ LOGGER imported successfully")
        
        print("\n✅ All imports successful! The bot should work on Render.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_imports()
    sys.exit(0 if success else 1)
