# PHANTOM: Undermining Mobile System Availability via Malformed Installation Metadata

<p align="center">
  <img src="Phantom.png" alt="PHANTOM" width="600">
</p>

## Overview

This repository contains artifacts for the paper **"PHANTOM: Undermining Mobile System Availability via Malformed Installation Metadata"**.

PHANTOM is a new class of attacks that exploits malformed package metadata to cause mobile system failures **without executing any code**. We identified **65 exploitable attack vectors** (33 Android, 32 iOS) with impacts ranging from service disruption to persistent boot loops.

## Repository Structure

```
├── CrashArtifactAndSourceCode/    # Pre-built APK/IPA + source code
├── CrashLogs/                     # System crash logs
├── DemonstrationVideos/           # Attack demonstration videos
└── EvaluationResults/             # Evaluation spreadsheets and supporting notes
```

The Android L3 signing-metadata artifacts include two pre-built APK/script
pairs, distinguished by the `signatures` and `signingInfo` suffixes.

## Impact Levels

| Level | Impact | Recovery |
|-------|--------|----------|
| L1 | Uninstallation Prevention | ADB uninstall |
| L2 | Partial Service Disruption | Reboot |
| L3 | Critical Service Disruption | Reboot / developer-tool removal |
| L4 | User Data Loss | Data lost |
| L5 | Complete System Failure | Factory reset / DFU reflash |

## Getting Started

**⚠️ WARNING: L3+ attacks can disrupt critical services, and L4/L5 cases can cause data loss. Use test devices only.**

### Quick Test (Android)

```bash
# Install pre-built APK
adb install CrashArtifactAndSourceCode/Android_L2_Partial_Service_Disruption.apk

# Observe SystemUI crash, then clean up
adb uninstall <package_name>
```

### Build from Source

Each artifact has a corresponding `.zip` with source code:

```bash
# Extract and modify as needed
unzip CrashArtifactAndSourceCode/Android_L2_Partial_Service_Disruption.zip

# Build with Android Studio, or use the Python helper script
cd CrashArtifactAndSourceCode
python Android_L3_Critical_Service_Disruption_signatures_build.py
python Android_L3_Critical_Service_Disruption_signingInfo_build.py
```

### iOS

Install the iOS `.ipa` artifacts through a valid installation channel (developer/enterprise signing, MDM, or `ios-deploy` for a connected test device):

```bash
ios-deploy -b CrashArtifactAndSourceCode/iOS_L2_Proximal_Attack_By_Airdrop.ipa
```

## Artifacts

| Platform | Files | Source |
|----------|-------|--------|
| Android L1-L5 | `Android_L{1..5}_*.apk` | `Android_L{1..5}_*.zip` |
| iOS L2 + sanitized L5 builder | `iOS_L2_Proximal_Attack_By_Airdrop.ipa` | `iOS_Source_Code_and_Builder.zip` |

## Ethical Notice

All vulnerabilities have been responsibly disclosed to Google and Apple. **Do not use maliciously.**

## License

MIT License - see [LICENSE](LICENSE)
